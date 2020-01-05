/*for å få til det må du bruke storen for å lagre hvilken klubb som er valgt, sånn at det blir tilgjengelig for neste view
- det er som en slags lokal "database" som alle komponentene kan bruke
 - også sier den fra til alle komponentene/sidene som bruker en attributt om når den oppdateres av andre komponenter/sider*/


export const state = () => ({
  header: {'X-Auth-Token': '20d659f26a5c462c9145cab84cfad9de'}, // 'Access-Control-Allow-Methods': "GET", 'Access-Control-Allow-Origin': "*", 'Access-Control-Allow-Headers':"x-auth-token, x-response-control", 'Content-Type': 'text/plain', mode: 'no-cors'},
  teamId: 0,
  logo: '',
  team: '',
  staff:[],
  competitions: [],
  matches: []
})

export const mutations = {
  setSelectedTeam(state, payload) {
    state.selectedTeam = payload
  }
}

export const actions = {

}
