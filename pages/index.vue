<template>
  <v-layout column justify-center>
    <v-flex xs12>
      <h1 style="text-align: center">Welcome to the football database!</h1>
    </v-flex>
    <v-flex xs4>
      <v-overflow-btn
        class="my-2"
        :items="areas"
        v-model="selectedCountryName"
        label="Choose country"
        editable
        item-value="text"
      ></v-overflow-btn>
    </v-flex>
    <v-flex xs4>
      <v-overflow-btn
        v-if="showTeamPicker"
        class="my-2"
        :items="teams"
        v-model="selectedTeam"
        label="Choose team"
        editable
        item-value="text"
      ></v-overflow-btn>
    </v-flex>
    <v-flex align-self-center>
      <v-btn large
        color="dark"
             @click="confirmTeam"
      >Enter</v-btn>
    </v-flex>
  </v-layout>

</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
    layout: 'frontpage',
    data () {
        return {
            areas: [],
            selectedCountry: '',
            selectedCountryName: '',
            selectedId: 0,
            selectedTeam: '',
            showTeamPicker: false,
            teams: ['Argentina','Brazil', 'Chile','Germany','Netherlands', 'Norway']
        }
    },
    beforeMount() {
        this.$axios.get('https://api.football-data.org/v2/competitions/', {headers: this.$store.state.header}).then((result) => {
            result.data.competitions.forEach((area) => {
                this.areas.push({'text': area.name, 'id': area.id})
            })
        })
    },
    watch: {
      selectedCountryName () {
          this.updateId()
          this.showTeamPicker = true
          this.getTeams()
          /*watch er en spesiell type metoder som kalles hver gang verdien til den du ser på endrer seg*/
      }
    },
    methods: {
        getTeams () {
            //this.teams = []
            //this.$axios.get('https://api.football-data.org/v2/competitions/' + this.selectedCountry.id + '/teams', {headers: this.$store.state.header}).then((result) => {
                //console.log(result)
               // result.data.teams.forEach((team) => {
                    //this.teams.push({'text': team.name, 'id': team.id})
                  //  console.log(this.teams);
               // })
            //})
        },
        updateId: function () {
            console.log("name: " + this.selectedCountryName);
            this.selectedCountry = this.areas.find((obj) => obj.name = this.selectedCountryName)
            var tempObj = this.areas.find((obj) => obj.name = this.selectedCountryName);
            console.log(tempObj);
            console.log("updateId: " + this.selectedCountry.name)
        },
        confirmTeam () {
            //proceed to next page
            if(this.selectedTeam != '') {
                this.$store.commit('setSelectedTeam', this.selectedTeam)
                this.$router.push('/home')
            }

            /*Prøv å logget objektet som returneres fra team spørringen*/

        }
    }
}
</script>
