def findHamPathsSubseq(g, start, end, hamPath=[]):
		"""
		Find all hamilton paths recursively that start with node 'start' and end with node 'end' in graph.
		Helper function to find all hamiltonian cycles
		"""
		hamPaths = list()
		# Base case: if the 'start' node and the 'end' node are equal, 
		# then the path is complete
		hamPath = hamPath + [start]
		if start == end:
			return [hamPath]

		# Iterate through the nodes that are connected to the start node
		for node in g[start]:
			# Check if the node is already in the path. If so then the node is not a part of the hamilton path, thus skip the node
			if node not in hamPath:
				# Since the node is not in the path, find and return the hamilton paths that stem from the base path 'hamPath' 
				hamPathSubseqs = findHamPathsSubseq(g, node, end, hamPath)
				# Iterate through the found paths and append them to the list of hamilton paths found
				for hamPath in hamPathSubseqs:
					hamPaths.append(hamPath)

		return hamPaths


def findAllHamCycles(g):
		"""
		Find all hamiltonian cycles in graph.
		A hamiltonian cycle is a path in a graph where the path visits every vertex exactly once
		and returns to itself at the end of the path
		
		"""
		hamCycles = list()

		for start in g:
				for end in g:
					# Assign the start and end nodes from g and find all hamilton paths that start with 'start and end with 'end'
					# Iterate through the returned paths
					hamPathSubseq = findHamPathsSubseq(g, start, end)
					for hamPath in hamPathSubseq:
						pathLength = len(hamPath)
						numGraphNodes = len(g)

						# Check that the number of vertexes in the graph is equal to the number of vertexes in the path
						if pathLength == numGraphNodes:
							pathStart = hamPath[0]
							pathEnd = hamPath[pathLength - 1]

							# Check if the start node of the path is accessible to the last node of the path
							# g[pathEnd] returns the list of nodes that path's end node is connected to

							# If the above is true, then the path is a cycle, thus append the start node to the end of the path completing the cycle,
							# and add the found path to the list of found cycles
							if pathStart in g[pathEnd]:
								hamPath.append(pathStart)
								hamCycles.append(hamPath)

		return hamCycles

if __name__ == '__main__':	
		g = {'1': ['2', '3'],
				 '2': ['1', '3','6'],
				 '3': ['2','5','6'],
				 '4': ['1','3','6'],
				 '5': ['1','2','3','4'],
				 '6': ['2', '4','5']}

		hamiltonCycles = findAllHamCycles(g)
		if len(hamiltonCycles) > 0:
						hamCycle = hamiltonCycles[0]

						print "Hamilton Cycle in graph"
						for node in hamCycle:
							print node,
		else:
				print "No hamilton cycles found in graph"
