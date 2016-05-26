package main 

import "github.com/ghodss/yaml"
import "path/filepath"
import "fmt"
import flag "github.com/ogier/pflag"
import "os"
import "encoding/json"
import "time"
import "strings"


type Node struct {
	ModTime time.Time  `json:"ModifiedTime"`
	IsLink bool 	   `json:"IsLink"`
	IsDir bool 		   `json:"IsDir"`
	LinksTo string 	   `json:"LinksTo"`
	Size int64		   `json:"Size"`
	Name string 	   `json:"Name"`
	Children []*Node   `json:"Children"`
	Parent   *Node     `json:"-"`
}

func printTextRep(dir []*Node, depth int) {
	for i := 0; i < len(dir); i++ {
		n := dir[i]
		if n.IsDir {
			printTabs(depth)
			fmt.Printf("%s/\n", n.Name)
			printTextRep(n.Children, depth + 1)

		} else {
			printTabs(depth)
			if !n.IsLink {
				fmt.Println(n.Name)
			} else {
				fmt.Printf("%s* (%s)\n", n.Name, n.LinksTo)
			}
		}
	}
}

func printTabs (n int) {
	for i := 0; i < n; i++ {
		fmt.Printf("  ")
	}
}


func readDirectory(root string, isRecursive bool) (result *Node, err error) {
	parents := make(map[string] *Node)

	walkFunc := func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		isLink := string(info.Mode().String()[0]) == "L"
		linksTo, e := os.Readlink(path)
		
		if e != nil {
			linksTo = ""
		}

		parents[path] = &Node{
			ModTime: info.ModTime(),
			IsLink: isLink,
			IsDir: info.IsDir(),
			LinksTo: linksTo,
			Size: info.Size(),
			Name: info.Name(),
			Children: make([]*Node, 0),
		}

		if isRecursive {
			return nil
		} else {
			if path == root || !info.IsDir() {
				return nil
			} else {
				return filepath.SkipDir
			} 
		}
	}

	if err = filepath.Walk(root, walkFunc); err != nil {
		return
	}
	
	for path, node := range parents {
		parentPath := filepath.Dir(path)
		parent, exists := parents[parentPath]

		if !exists {
			result = node
		} else {
			node.Parent = parent
			parent.Children = append(parent.Children, node)
		}
	}

	return 
}



func main() {
	var pathFlag *string = flag.String("path", "", "Path to folder that bclister will list files from. Required")
	var recursiveFlag *bool = flag.Bool("recursive", false, "When set, list files recursively")
	var outputFlag *string = flag.String("output", "text", "Output format. Options: json, yaml, text. Default: text")
	flag.Parse()


	if *pathFlag == "" {
		fmt.Println("The path flag is required. Please provide a path to be evaluated.")
		return
	}

	*pathFlag, _ = filepath.Abs(*pathFlag)


	result, readErr := readDirectory(*pathFlag, *recursiveFlag)

	if readErr != nil {
		fmt.Println("The path provided does not exist. Please provide a valid path")
		return
	}

	if strings.ToLower(*outputFlag) == "json" {
		b, err := json.MarshalIndent(result.Children, "", "    ")
		if err != nil {
			fmt.Println("error", err)
			return 
		}

		os.Stdout.Write(b)
		fmt.Println()

	} else if strings.ToLower(*outputFlag) == "yaml" {
		y, err := yaml.Marshal(result.Children)

		if err != nil {
			fmt.Println("error", err)
			return
		}

		os.Stdout.Write(y)
		fmt.Println()

	} else if strings.ToLower(*outputFlag) == "text" {
		fmt.Println(*pathFlag)
		printTextRep(result.Children, 1)

	} else {
		flag.Usage()
	}

}
