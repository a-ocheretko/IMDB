<template>
<main>
  <div class="px-4 py-5 my-5">
    <div class="container">
      <div class="d-flex justify-content-center h-100">
        <div class="card">
          <div class="card-header">
            <h3>Sign In</h3>
<!--            <div class="d-flex justify-content-end social_icon">-->
<!--              <span><i class="fab fa-facebook-square"></i></span>-->
<!--              <span><i class="fab fa-google-plus-square"></i></span>-->
<!--              <span><i class="fab fa-twitter-square"></i></span>-->
<!--            </div>-->
          </div>
          <div class="card-body">
            <form @submit="loginUser">
              <div class="input-group form-group">
                <div class="input-group-prepend">
                  <span class="input-group-text"><i class="fas fa-user"></i></span>
                </div>
                <input type="email" class="form-control" placeholder="email" v-model="data.email" required="required">
                {{error.email}}
              </div>
              <div class="input-group form-group">
                <div class="input-group-prepend">
                  <span class="input-group-text"><i class="fas fa-key"></i></span>
                </div>
                <input type="password" class="form-control" placeholder="password" v-model="data.password" required="required">
                {{error.password}}
              </div>
              <div class="form-group">
                {{error.details}}
                <input type="submit" value="Login" class="btn float-right login_btn">
              </div>
            </form>
          </div>
          <div class="card-footer">
            <div class="d-flex justify-content-center links">
              Don't have an account?<a href="/accounts/register">Register</a>
            </div>
<!--            <div class="d-flex justify-content-center">-->
<!--              <a href="#">Forgot your password?</a>-->
<!--            </div>-->
          </div>
        </div>
      </div>
    </div>
  </div>
</main>
</template>

<script>
import {useUserStore} from "@/stores/user";
import {apiFetch} from "@/utils/api"
export default {
  name: "LoginForm",
  data(){
    return {
      data: {
        email: '',
        password: ''
      },
      error: {
      }
    }
  },
  methods: {
    async loginUser(e) {
      e.preventDefault()
      e.stopPropagation()


      const resp = await apiFetch('/api/v1/auth/token/',
      {
            method: 'POST',
            body: JSON.stringify(this.data)
          }
      )

      if (resp.status !== 200) {
        this.error = await resp.json()
        return
      } else {
        const data = await resp.json()
        localStorage.setItem('userToken', data.access)
        await useUserStore().fetchUser();
        location.href = '/';
      }
    }
  }
}
</script>

<style scoped>

html,body{
background-size: cover;
background-repeat: no-repeat;
height: 100%;
font-family: 'Numans', sans-serif;
}

.container{
height: 100%;
align-content: center;
}

.card{
height: 280px;
margin-top: auto;
margin-bottom: auto;
width: 400px;
background-color: rgba(0,0,0,0.5) !important;
}

/*.social_icon span{*/
/*font-size: 50px;*/
/*margin-left: 10px;*/
/*color: #FFC312;*/
/*}*/
/**/
/*.social_icon span:hover{*/
/*color: white;*/
/*cursor: pointer;*/
/*}*/

.card-header h3{
color: white;
}

/*.social_icon{*/
/*position: absolute;*/
/*right: 20px;*/
/*top: -9px;*/
/*}*/

.input-group-prepend span{
width: 50px;
background-color: #FFC312;
color: black;
border:0 !important;
}

input:focus{
outline: 0 0 0 0  !important;
box-shadow: 0 0 0 0 !important;
}

.login_btn{
color: black;
background-color: #FFC312;
width: 100px;
}

.login_btn:hover{
color: black;
background-color: white;
}

.links{
color: white;
}

.links a{
margin-left: 4px;
}
</style>