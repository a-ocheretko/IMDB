<template>
  <table class="table table-fixed">
    <tbody class="table-bordered" style="border: hidden">
      <td style="background-color: rgba(0,0,0,0.03); position: relative; width: 19%; height: 340px; float: left;
      margin: 0.5%; border-width: medium; border-radius: 7px" v-for="p in persons" :style="{color}">
        <td style="border: hidden;">
          <a href="#"><h4 style="position: absolute; top: 5%"><b>{{ p.name }}</b></h4></a>
<!--          <div v-if="m.director.length !== 0" style="position: absolute; left: 0; top: 35%">-->
<!--            <td style="border: hidden" v-for="d in m.director" v-show="d" :style="{color}">-->
<!--              <td style="border: hidden">-->
<!--                <a href="#">{{ d }}</a>-->
<!--              </td>-->
<!--            </td>-->
<!--          </div>-->
          <div v-if="p.birth_year || p.death_year" style="position: absolute; left: 5%; bottom: 20%">
            <td style="border: hidden">
              {{ p.birth_year }} - {{ p.death_year }}
            </td>
          </div>
        </td>
      </td>
    </tbody>
  </table>
  <table style="margin: auto;">
    <tbody>
      <td v-if="currentPage===firstPage" style="position:absolute; left: 26%;">
        <button class="mw-100 btn btn-sm btn-danger" disabled="disabled" style="margin: 1px; width: 43px; color: white"
                type="button">
          <b>&lt&lt</b>
        </button>
      </td>
      <td v-else style="position:absolute; left: 26%;" @click="redirectTo(firstPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-danger" style="margin: 1px; width: 43px; color: white" type="button">
            <b>&lt&lt</b>
          </button>
        </a>
      </td>
      <td v-if="currentPage > firstPage" style="position:absolute; left: 30%;" @click="redirectTo(--currentPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-info" style="margin: 1px; width: 43px; color: white" type="button">
            <b>&lt</b>
          </button>
        </a>
      </td>
      <td v-else style="position:absolute; left: 30%;">
        <button class="mw-100 btn btn-sm btn-info" disabled="disabled" style="margin: 1px; width: 43px; color: white"
                type="button">
          <b>&lt</b>
        </button>
      </td>
      <td v-for="page in pagesArray" @click="redirectTo(page)" :style="color">
        <a href="#">
          <button v-if="currentPage===page" class="mw-100 btn btn-sm btn-warning" style="margin: 1px; width: 43px;
          color: white" type="button">
            {{ page }}
          </button>
          <button v-else class="mw-100 btn btn-sm btn-primary" style="margin: 1px; width: 43px; color: white"
                  type="button">
            {{ page }}
          </button>
        </a>
      </td>
      <td v-if="currentPage < lastPage" style="position:absolute; right: 30%;" @click="redirectTo(++currentPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-info" style="margin: 1px; width: 43px; color: white" type="button">
            <b>&gt</b>
          </button>
        </a>
      </td>
      <td v-else style="position:absolute; right: 30%;">
        <button class="mw-100 btn btn-sm btn-info" disabled="disabled" style="margin: 1px; width: 43px; color: white"
                type="button">
          <b>&gt</b>
        </button>
      </td>
      <td v-if="currentPage===lastPage" style="position:absolute; right: 26%;">
        <button class="mw-100 btn btn-sm btn-danger" disabled="disabled" style="margin: 1px; width: 43px; color: white"
                type="button">
          <b>&gt&gt</b>
        </button>
      </td>
      <td v-else style="position:absolute; right: 26%;" @click="redirectTo(lastPage)">
        <a href="#">
          <button class="mw-100 btn btn-sm btn-danger" style="margin: 1px; width: 43px; color: white" type="button">
            <b>&gt&gt</b>
          </button>
        </a>
      </td>
    </tbody>
  </table>
</template>

<script>

export default {
  name: "PersonsList",
  props: {
    color: String
  },
  data() {
    return {
      persons: [],
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
        window.location.href=`/persons/?page=${page}`
      }
    },
  async beforeMount() {

    const params = new URLSearchParams(window.location.search)

    this.currentPage = parseInt(params.get('page'))

    const response = await fetch(`/api/v1/imdb/person/?page=${this.currentPage}`)

    if (response.ok) {
      const results = await response.json()
      this.lastPage = Math.ceil(results.count / this.paginationSize)
      this.persons = results.results
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
