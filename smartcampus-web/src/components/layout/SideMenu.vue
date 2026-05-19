<script setup lang="ts">
import items from "../../helpers/menuItems";
</script>

<template>
  <aside id="side-menu" role="menu">
    <nav class="side-menu-nav">
      <ul>
        <li
          v-for="(item, key) in items"
          :key="item.label.concat(key.toString())"
        >
          <span v-if="item.items">
            <span>{{ item.label }}</span>
            <ul>
              <li
                v-for="(child, childKey) in item.items"
                :key="child.label.concat(childKey.toString())"
              >
                <router-link
                  v-slot="{ href, navigate }"
                  :to="child.route"
                  custom
                >
                  <a class="item-link" :href="href" @click="navigate">
                    <i :class="child.icon" />
                    <span>{{ child.label }}</span>
                  </a>
                </router-link>
              </li>
            </ul>
          </span>
          <router-link
            v-else
            v-slot="{ href, navigate }"
            :to="item.route"
            custom
          >
            <a class="item-link" :href="href" @click="navigate">
              <i :class="item.icon" />
              <span>{{ item.label }}</span>
            </a>
          </router-link>
        </li>
      </ul>
      <span class="end-options">
        <span class="sign-out-option item-link">
          <i class="pi pi-sign-out" />
          <span>Sign Out</span>
        </span>
      </span>
    </nav>
  </aside>
</template>

<style scoped lang="scss">
#side-menu {
  padding: 0.25rem;
  border-right: 1px solid #cecece;

  .item-link {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    text-decoration: none;
  }

  .side-menu-nav {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;

    ul {
      list-style: none;
      padding: 0;
      margin: 0;

      li {
        padding: 0.5rem 1rem;
        min-width: 9.375rem;

        &:hover {
          background-color: #cecece;
        }
      }
    }

    .end-options {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      padding-bottom: 1rem;

      .sign-out-option {
        cursor: pointer;
        padding: 0.5rem 1rem;

        &:hover {
          background-color: #cecece;
        }
      }
    }
  }
}
</style>
