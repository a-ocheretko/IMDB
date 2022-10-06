<template>
 <nav class="navbar navbar-expand-lg" style="background-color: #FFC312">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">Home</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/movies/?page=1">Movies</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/persons/?page=1">Persons</a>
        </li>
      </ul>
        <UserBadge />
    </div>
  </div>
</nav>
</template>

<script>
import UserBadge from "./UserBadge.vue";
export default {
  name: "NavBar",
  components: {UserBadge}
}
</script>

<style scoped>

</style>
