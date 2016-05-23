<template>
  <div class="mdl-cell mdl-card mdl-shadow--4dp portfolio-card">
    <mdl-button class="randstarshipBtn" v-mdl-ripple-effect colored icon raised v-on:click="fetchRandomStarship">
      <i class="material-icons">send</i> Random starship
    </mdl-button>
    <mdl-textfield floating-label="Name" :value.sync="shipData.name"></mdl-textfield>
    <mdl-textfield floating-label="Model" :value.sync="shipData.model"></mdl-textfield>
    <mdl-textfield floating-label="Starship Class" :value.sync="shipData.starship_class"></mdl-textfield>
    <mdl-textfield floating-label="Manufacturer" :value.sync="shipData.manufacturer"></mdl-textfield>
    <mdl-textfield floating-label="Cost in credits" :value.sync="shipData.cost_in_credits"></mdl-textfield>
    <mdl-textfield floating-label="Length" :value.sync="shipData.length"></mdl-textfield>
    <mdl-textfield floating-label="Hyperdrive rating" :value.sync="shipData.hyperdrive_rating"></mdl-textfield>
    <mdl-textfield floating-label="Cargo Capacity" :value.sync="shipData.cargo_capacity"></mdl-textfield>
  </div>
</template>

<script>
import ship from '../api/starship';
import { MdlButton, MdlTextfield, directives } from 'vue-mdl';

export default {
  components: {
    MdlButton,
    MdlTextfield,
  },
  directives,
  data() {
    return {
      shipData: {
        name: '',
        model: '',
        starship_class: '',
        manufacturer: '',
        cost_in_credits: '',
        length: '',
        hyperdrive_rating: '',
        cargo_capacity: '',
      },
    };
  },
  methods: {
    fetchRandomStarship() {
      const randomShipId = Math.floor((Math.random() * 37) + 1);
      ship.fetch(randomShipId).then((shipData) => {
        this.shipData = Object.assign(this.shipData, shipData);
      });
    },
  },
};
</script>
