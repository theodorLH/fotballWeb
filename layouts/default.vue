<template>
  <v-app
    light
  >
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
      class="deep-purple accent-4"
      dark
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
      class="deep-purple accent-4"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-arrow-left',
          title: 'Choose a new team',
          to: '/'
        },
        {
          //icon: 'home',
          title: 'Home',
          to: '/home'
        },
          {
              //icon: 'info',
              title: 'Match schedule',
              to: '/information'
          }
          /*{
              //icon: 'event',
              title: 'Player information',
              to: './schedule'
          }*/
      ],
      miniVariant: false,
      right: true,
      title: 'Football Central'
    }
  }
}
</script>
