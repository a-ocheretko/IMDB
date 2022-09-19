<template>
<div></div>
  <ul>
    <li v-for="movie in movies" :style="{color}"> {{ movie.name }} </li>
  </ul>

</template>

<script>
export default {
  name: "MoviesList",
  props: {
    color: String
  },
  data() {
    return {
      movies: []
    }
  },
  async beforeMount() {
    const response = await fetch('/api/v1/imdb/movie/')

    if (response.ok) {
      const results = await response.json()
      this.movies = results.results

    }
  }

}
</script>

<style scoped>
</style>