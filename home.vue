<template>
  <div>
    <v-flex xs12> <h1>{{team}}</h1>
    </v-flex>
    <v-flex xs12>
      <h1 style="text-align: center">Team and squad information</h1>
    </v-flex>

  </div>
</template>

<script>
    export default {
        layout: 'default',
        data () {
            return{
                Players: []
            }
        },
        beforeMount() {
            this.$axios.get('https://api.football-data.org/v2/teams/{id}', {headers: this.$store.state.header}).then((result) => {
                result.data.team.forEach((info) => {
                    this.team.push({'text': info.name, 'id': info.id})
                })
            })
        }
    }
</script>



