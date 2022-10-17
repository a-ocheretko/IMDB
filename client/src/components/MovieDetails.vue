<template>
  <div>
    <h2 style="position: absolute; top: 17%; left: 30%"><b>{{ data.name }}</b></h2>
  </div>
  <td style="position: absolute; top: 27%; left: 30%">
    <td style="border: hidden; padding: 3px;" v-for="genre in data.genres" :style="{color}">
      <m-d-b-badge badge="success" pill class="d-inline">{{ genre }}</m-d-b-badge>
    </td>
  </td>
  <div style="position: absolute; top: 36%; left: 30%">
    <tr style="border: hidden;" v-for="d in data.director" :style="{color}">
      <td style="border: hidden">
        <b>{{ d }}</b>
      </td>
    </tr>
  </div>
  <div v-if="data.year" style="position: absolute; top:44%; left: 30%">
    <td style="border: hidden">
      {{ data.year }}
    </td>
  </div>
  <table style="position: absolute; top:57%; left: 12%; width: 35%">
    <tbody>
      <td style="position: absolute; top:-40px; left: 0;">
        <b>Name</b>
      </td>
      <td>
        <tr style="border: hidden; height: 30px" v-for="name in personsList" :style="{color}">
          <td>
            {{ name }}
          </td>
        </tr>
      </td>
      <td style="position: absolute; left: 50%; top:-40px;">
        <b>Position</b>
      </td>
      <td style="position: absolute; left: 50%; top: 0;">
        <tr style="border: hidden; height: 30px" v-for="p in data.position" :style="{color}">
          <td>
            {{ p }}
          </td>
        </tr>
      </td>
      <td style="position: absolute; left: 100%; top:-40px;">
        <b>Role</b>
      </td>
      <td style="position: absolute; left: 100%; top:0; width: fit-content">
        <tr style="border: hidden; height: 30px" v-for="r in roles" :style="{color}">
          <td v-for="item in r" :style="{color}">
            <div v-if="item === 'N/A'"><br></div>
            <div v-else>{{ item }}</div>
          </td>
        </tr>
      </td>
    </tbody>
  </table>
</template>

<script>
import { MDBTable, MDBBtn, MDBBadge } from 'mdb-vue-ui-kit'

export default {
  components: {
      MDBTable,
      MDBBtn,
      MDBBadge
  },
  name: "MovieDetails",
  props: {
    color: String
  },
  data() {
    return {
      data: [],
      personsList: [],
      roles: [],
      currentPage: 0,
    }
  },
  async beforeMount() {

    const path = window.location.pathname.split('/')
    this.currentPage = path[2]
    const response = await fetch(`/api/v1/imdb/movie/${this.currentPage}`)

    if (response.ok) {
      this.data = await response.json()
    }

    for (let person in this.data.persons) {
      const personResponse = await fetch(`/api/v1/imdb/person/${this.data.persons[person]}`)
      if (personResponse.ok) {
        const personData = await personResponse.json()
        this.personsList.push(personData.name)
      }
    }

    for (let role in this.data.role) {
      if (this.data.role[role] === null) {
        this.roles.push(['N/A'])
      }
      else {
        this.roles.push(this.data.role[role])
      }
    }
  }
}
</script>

<style scoped>

</style>
