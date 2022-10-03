<template>
<div></div>
  <ul>
    <li v-for="person in persons" :style="{color}">
      <a href="#">{{ person.name }}</a>
    </li>
  </ul>

</template>

<script>
export default {
  name: "PersonsList",
  props: {
    color: String
  },
  data() {
    return {
      persons: []
    }
  },
  async beforeMount() {
    const response = await fetch('/api/v1/imdb/person/')

    if (response.ok) {
      const results = await response.json()
      this.persons = results.results

    }
  }

}
</script>

<style scoped>
</style>