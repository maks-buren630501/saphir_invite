<template>
  <v-card width="600" style="position:absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);">
    <v-card-title>Title card</v-card-title>
    <v-card-subtitle>Subtitle card</v-card-subtitle>
    <v-card-text>
      <v-form>
        <v-text-field autofocus placeholder="Request" label="Please enter your input" type="number">
          <template v-slot:append-outer>
            <v-btn icon>
              <v-icon>mdi-check</v-icon>
            </v-btn>
          </template>
        </v-text-field>
      </v-form>

    </v-card-text>
    <template v-if="result">
      <v-card-title>Result:</v-card-title>

      <v-card-text>
        <v-skeleton-loader v-if="loading" type="text, text, text, text"/>
        <template v-else>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab consequuntur esse, laudantium repellat ullam vero. Ab
          deleniti et exercitationem, impedit iure laboriosam odio officia possimus quas, quisquam rem sequi tenetur ullam
          velit voluptatem. Ab ad autem, dolor eaque eius enim error est et eveniet fuga harum illo illum itaque labore
          laboriosam molestiae nam neque nisi non officia quae, quis quo quod quos rem, sequi soluta suscipit velit voluptas
          voluptatum. Blanditiis officiis placeat sint voluptate. Accusantium aliquam, assumenda atque debitis, ea enim esse
          eveniet expedita explicabo impedit, necessitatibus nemo nisi non odio perspiciatis ratione repudiandae saepe ullam
          ut vel vero voluptatibus.
        </template>
      </v-card-text>
    </template>
    <v-card-actions>
      <v-btn @click="show = !show" text width="100%">Description</v-btn>
      <v-spacer/>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for
          sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you
          add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    show: false,
    loading: true,
    result: null,
  })
}
</script>

<style>
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}
</style>
