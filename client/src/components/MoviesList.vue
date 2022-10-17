<template xmlns="http://www.w3.org/1999/html">
  <table class="table table-fixed">
    <tbody class="table-bordered" style="border: hidden">
      <td style="background-color: rgba(0,0,0,0.03); position: relative; width: 19%; height: 340px; float: left;
      margin: 0.5%; border-width: medium; border-radius: 7px" v-for="m in movies" :style="{color}">
        <td style="border: hidden;" @click="redirectToMovie(m.id)">
          <a href="#"><h4 style="position: absolute; top: 5%"><b>{{ m.name }}</b></h4></a>
          <div v-if="m.director.length !== 0" style="position: absolute; left: 0; top: 35%">
            <td style="border: hidden" v-for="d in m.director" v-show="d" :style="{color}">
              <td style="border: hidden">
                <b style="color: royalblue">{{ d }}</b>
              </td>
            </td>
          </div>
          <div v-if="m.year" style="position: absolute; left: 5%; bottom: 20%">
            <td style="border: hidden">
              {{ m.year }}
            </td>
          </div>
          <div v-if="m.genres" style="position: absolute; left: 3%; bottom: 6%">
            <td style="border: hidden; padding: 3px;" v-for="genre in m.genres" :style="{color}">
              <m-d-b-badge badge="success" pill class="d-inline">{{ genre }}</m-d-b-badge>
            </td>
          </div>
        </td>
      </td>
    </tbody>
  </table>
  <table style="margin: auto;">
    <tbody>
      <td v-if="currentPage===firstPage" style="position:absolute; left: 23%;">
        <button class="mw-100 btn btn-sm btn-danger" disabled="disabled" style="margin: 1px; width: 50px; color: white"
                type="button">
          <b>First</b>
        </button>
      </td>
      <td v-else style="position:absolute; left: 23%;" @click="redirectTo(firstPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-danger" style="margin: 1px; width: 50px; color: white" type="button">
            <b>First</b>
          </button>
        </a>
      </td>
      <td v-if="currentPage > firstPage" style="position:absolute; left: 27%;" @click="redirectTo(--currentPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-info" style="margin: 1px; width: 50px; color: white" type="button">
            <b>Prev</b>
          </button>
        </a>
      </td>
      <td v-else style="position:absolute; left: 27%;">
        <button class="mw-100 btn btn-sm btn-info" disabled="disabled" style="margin: 1px; width: 50px; color: white"
                type="button">
          <b>Prev</b>
        </button>
      </td>
      <td v-for="page in pagesArray" @click="redirectTo(page)" :style="color">
        <a href="#">
          <button v-if="currentPage===page" class="mw-100 btn btn-sm btn-warning" style="margin: 1px; width: 50px;
          color: white" type="button">
            {{ page }}
          </button>
          <button v-else class="mw-100 btn btn-sm btn-primary" style="margin: 1px; width: 50px; color: white"
                  type="button">
            {{ page }}
          </button>
        </a>
      </td>
      <td v-if="currentPage < lastPage" style="position:absolute; right: 27%;" @click="redirectTo(++currentPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-info" style="margin: 1px; width: 50px; color: white" type="button">
            <b>Next</b>
          </button>
        </a>
      </td>
      <td v-else style="position:absolute; right: 27%;">
        <button class="mw-100 btn btn-sm btn-info" disabled="disabled" style="margin: 1px; width: 50px; color: white"
                type="button">
          <b>Next</b>
        </button>
      </td>
      <td v-if="currentPage===lastPage" style="position:absolute; right: 23%;">
        <button class="mw-100 btn btn-sm btn-danger" disabled="disabled" style="margin: 1px; width: 50px; color: white"
                type="button">
          <b>Last</b>
        </button>
      </td>
      <td v-else style="position:absolute; right: 23%;" @click="redirectTo(lastPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-danger" style="margin: 1px; width: 50px; color: white" type="button">
            <b>Last</b>
          </button>
        </a>
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
  name: "MoviesList",
  props: {
    color: String
  },
  data() {
    return {
      movies: [],
      currentPage: null,
      paginationSize: 10,
      paginationStep: 5,
      paginationStart: 1,
      firstPage: 1,
      lastPage: null,
      pagesArray: []
    }
  },
    methods: {
      redirectTo(page){
        window.location.href=`/movies/?page=${page}`
      },
      redirectToMovie(id){
        window.location.href=`/movies/${id}`
      }
    },
  async beforeMount() {

    const params = new URLSearchParams(window.location.search)
    this.currentPage = parseInt(params.get('page'))
    const response = await fetch(`/api/v1/imdb/movie/?page=${this.currentPage}`)

    if (response.ok) {
      const results = await response.json()
      this.lastPage = Math.ceil(results.count / this.paginationSize)
      this.movies = results.results
    }

    if (this.currentPage > this.paginationStart + this.paginationStep) {
      this.paginationStart = this.currentPage - this.paginationStep
      this.currentPage = parseInt(params.get('page'))
    }

    if (this.paginationStart > this.lastPage - this.paginationSize) {
        this.paginationStart = this.lastPage - this.paginationSize
    }

    if (this.lastPage - this.paginationStart > this.paginationSize) {
      for (let i = this.paginationStart; i < this.paginationStart + this.paginationSize; i++) {
        this.pagesArray.push(i)
      }
    }
    else {
      for (let i = this.paginationStart + 1; i < this.lastPage + 1; i++) {
        this.pagesArray.push(i)
      }
    }
  }
}
</script>

<style scoped>

</style>
