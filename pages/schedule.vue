<template>
  <v-layout column justify-center>
    <v-flex xs12>
      <h1 style="text-align: center">Upcoming match fixtures</h1>
    </v-flex>

    <v-flex xs12>
      <h1 style="text-align: center">Previous match results</h1>
    </v-flex>

  </v-layout>
</template>

<script>
    export default {
        layout: 'default',
        data () {
            return{
                matches: []
            }
        },
        /*beforeMount() {
            this.$axios.get('https://api.football-data.org/v2/teams/86/matches?status=SCHEDULED', {headers: this.$store.state.header}).then((result) => {
                ///v2/teams/{id}/matches/
                result.data.matches.forEach((match) => {
                    this.matches.push({'text': area.name, 'id': area.id})
                })
            })
        },*/
        methods: {
            updateInfo() {

            }
        }
    }
</script>

<style scoped>

</style>
