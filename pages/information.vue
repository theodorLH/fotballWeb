<template>
  <div>
    <v-flex xs12>
      <h1 style="text-align: center">Match Fixtures</h1>
    </v-flex>

  </div>
</template>

<script>
    export default {
        layout: 'default',
        data () {
            return{
                matches: []
            }
        },
        beforeMount() {
            this.$axios.get('https://api.football-data.org/v2/teams/{id}', {headers: this.$store.state.header}).then((result) => {
                result.data.matches.forEach((info) => {
                    this.matches.push({'text': info.name, 'id': info.id})
                })
            })
        }
    }
</script>

