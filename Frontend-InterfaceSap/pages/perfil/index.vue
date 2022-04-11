// Historico

<template>
  <div class="cont">
    <headers />
    <div class="principal">
      <div class="base">
        <div class="line">
        <h1>Perfil</h1>
        <div id="btn-div" tag="img" @click="dropMenuToggle">
          <img src="@/assets/icon/list-solid.svg" />
        </div>
        </div>

        <div class="menu">
          <div v-if="dropMenu" :class="['sidebar', { active: dropMenu }]" id="dropDownMenu">
            <NuxtLink class="nav" to="/sucata">Sucata</NuxtLink>
            <NuxtLink class="nav" to="/sucata">Produtos</NuxtLink>
          </div>

          <hr/>
          <img src="perfil.png" alt="" id="foto_perfil" />
          <h1>Nome completo</h1>
        </div>

        <div class="info">
          <section class="colun1">
            <h4>User</h4>
            <p>teste</p>

            <h4>Email</h4>
            <p>teste@gmail.com</p>
          </section>
          <section class="colun2">
            <h4>EDV</h4>
            <p>9999999</p>

            <h4>Responsavel</h4>
            <p>aaaaaaaaa</p>
          </section>
        </div>
      </div>
    </div>
    <footers />
  </div>
</template>

<script>
export default {
  name: 'home',
  data: function () {
    return {
      menuFlyout: false,
      dropMenu: false,
    }
  },
  methods: {
    dropMenuToggle: function () {
      this.dropMenu = !this.dropMenu
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/perfil/perfil.scss';
</style>
