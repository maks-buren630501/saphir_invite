<template>
  <v-card width="600" style="position:absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);">
    <v-card-title>Глинка Андрей Владимирович</v-card-title>
    <v-card-subtitle>Форма проверки алгоритма</v-card-subtitle>
    <v-card-text>
      <v-form ref="form" v-model="valid" onSubmit="return false;">
        <v-text-field
            v-model="value"
            :rules="rules"
            @input="result = ''"
            @keyup.enter="execute()"
            autofocus required
            placeholder="Введите только целое положительное число"
            label="Введите число"
            class="pb-0"
        >
          <template v-slot:append-outer>
            <v-btn @click="execute" icon :loading="loading" :disabled="!valid">
              <v-icon>mdi-check</v-icon>
            </v-btn>
          </template>
        </v-text-field>
      </v-form>

    </v-card-text>
    <v-slide-y-transition>
      <v-card-title v-if="result">Ответ: {{ result }}</v-card-title>
    </v-slide-y-transition>
    <v-card-actions>
      <v-btn @click="showTests = !showTests" text width="100%">Тестовые данные</v-btn>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="showTests">
        <v-divider></v-divider>
        <v-card-text>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class="text-left">Входные данные</th>
                <th class="text-left">Ответ</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(item, i) in examples" :key="i">
                <td>{{ item.input }}</td>
                <td>{{ item.result }}</td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    value: '',
    showTests: false,
    loading: false,
    result: null,
    valid: true,
    rules: [
      value => !!value || 'Поле должно быть заполнено.',
      value => {
        const valid = true // Необходимо написать валидатор для заданного условия
        return valid || 'Проверьте введенные данные'
      },
    ],
    examples: [
      {
        input: '4',
        result: '[1, 4]'
      },
      {
        input: '9',
        result: '[1, 4, 9]'
      },
      {
        input: '16',
        result: '[ 1, 4, 9, 16 ]'
      },
    ]
  }),
  methods: {
    execute() {
      if(this.$refs.form.validate()) {
        this.loading = true
        this.axios.get('state_on_switches', {params: {num: this.value}})
          .then(r => this.result = r.data.message)
          .catch(e => this.result = 'Ошибка выполнения')
          .finally(() => this.loading = false)
      }
    }
  }
}
</script>

<style>
</style>