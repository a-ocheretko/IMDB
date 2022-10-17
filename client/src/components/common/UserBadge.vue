<template>
  <div>
    <div v-if="userStore.user">
      <b>{{ userStore.getUserName }}</b>
      <a href="#" @click="logOut"><button class="mw-100 btn btn-sm btn-primary" style="margin: 5px; color: white" type="button"><b>Log Out</b></button></a>
    </div>
    <div v-else>
      <RouterLink to="/login"><button class="mw-100 btn btn-sm btn-primary" style="margin: 5px; color: white" type="button"><b>Log In</b></button></RouterLink>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "../../stores/user"

export default {
  name: "UserBadge",
  setup() {
    const userStore = useUserStore();
    return {
      userStore
    }
  },
  data() {
    return {
      user: this.userStore.user
    }
  },
  methods: {
    logOut() {
      this.userStore.logOut()
    },
    logIn() {
      this.userStore.logIn()
    }
  },
}
</script>

<style scoped>

</style>