<template>
  <v-card width="600" style="position:absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);">
    <v-card-title>Гуменюк Александр Сергеевич</v-card-title>
    <v-card-subtitle>Форма проверки алгоритма</v-card-subtitle>
    <v-card-text>
      <v-form ref="form" v-model="valid" onSubmit="return false;">
        <v-text-field
          v-model="value"
          :rules="rules"
          @input="result = ''"
          @keyup.enter="execute()"
          autofocus required
          placeholder="Пример: 1 2 ... n"
          label="Введите список"
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
      value => ( /^([0-9\s]+)$/.test(value)) || 'Проверьте введенные данные',

    ],
    examples: [
      {
        input: '1 2 3 4 5',
        result: '4'
      },
      {
        input: '1 2 3 5 7 9',
        result: '5'
      },
      {
        input: '0 5 8 9 11 13 14 16 17 19',
        result: '10'
      },
      {
        input: '0 1 2 3 5 6 7 11 13 15 17 19',
        result: '17'
      }
    ]
  }),
  methods: {
    execute() {
      if(this.$refs.form.validate()) {
        this.loading = true
        this.value = this.value.replace(/ {1,}/g," "); //удаление двойных пробелов , если такие имеются
        this.value = this.value.trim() //удаление последнего пробела, если он имеется
        this.axios.post('/progression', {list_nums: this.value.split(' ')})
        .then(r => this.result = r.data.num)
        .catch(e => this.result = 'Ошибка выполнения')
        .finally(() => this.loading = false)
      }
    }

  }
}
</script>

<style>
</style>
