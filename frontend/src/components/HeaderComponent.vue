<template>
  <div>
    <TopBarComponent />
    <NavBarComponent />
  </div>
</template>

<script>
import TopBarComponent from '@/components/TopBarComponent'
import NavBarComponent from './NavBarComponent.vue'

export default {
  name: 'HeaderComponent',
  components: {
    TopBarComponent,
    NavBarComponent
  }
}
</script>
