<template>
  <v-card width="600" style="position:absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);">
    <v-card-title>Дубицкий Антон Михайлович</v-card-title>
    <v-card-subtitle>Форма проверки алгоритма</v-card-subtitle>
    <v-card-text>
      <v-form ref="form" v-model="valid" @keyup.enter="execute()" onSubmit="return false;">
        <v-text-field
          v-model="value"
          :rules="rulesValue"
          @input="result = ''"
          autofocus required
          placeholder="Введите массив целых положительных чисел"
          label="Введите числа"
          class="pb-0"
        />
        <v-text-field
          v-model="bonus"
          :rules="rulesBonus"
          @input="result = ''"
          autofocus required
          placeholder="Введите целое положительное число"
          label="Введите число бонусов"
          class="pb-0"
        />
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-end">
      <v-btn @click="execute" :disabled="!valid" text>Выполнить</v-btn>
    </v-card-actions>
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
    bonus: '',
    showTests: false,
    loading: false,
    result: null,
    valid: true,
    rulesValue: [
      value => !!value || 'Поле должно быть заполнено.',
      value => {
        for (var i = 0; i < value.length; i++) {
          if (value[i] == '$' || value[i] == '^' || 
              value[i] == '*' || value[i] == '(' || 
              value[i] == ')' || value[i] == '+' ||
              value[i] == '.' || value[i] == '?' ||
              value[i] == '[') {
                return 'Поле может содержать только целые положительные числа, введенные через пробел'
          }
          const tmp = new RegExp (value[i])
          if(!tmp.test(' 0 1 2 3 4 5 6 7 8 9 ')) {
            return 'Поле может содержать только целые положительные числа, введенные через пробел'
          }
        }
        if (value[0] == ' ' || value[value.length - 1] == ' ') {
          return 'Первым и последним символом должно быть число'
        }
        const valid = true
        return valid || 'Проверьте введенные данные'
      },
    ],
    rulesBonus: [
      value => !!value || 'Поле должно быть заполнено.',
      value => {
        for (var i = 0; i < value.length; i++) {
          if (value[i] == '$' || value[i] == '^' || 
              value[i] == '*' || value[i] == '(' || 
              value[i] == ')' || value[i] == '+' ||
              value[i] == '.' || value[i] == '?' ||
              value[i] == '[') {
                return 'Поле может содержать только целые положительные числа, введенные через пробел'
          }
          const tmp = new RegExp (value[i])
          if(!tmp.test(' 0 1 2 3 4 5 6 7 8 9 ')) {
            return 'Поле может содержать только целые положительные числа, введенные через пробел'
          }
        }
        const tmp2 = value.split(' ') 
        if (tmp2.length > 1) {
          return 'Поле может содержать только одно положительное число'
        }
        const valid = true
        return valid || 'Проверьте введенные данные'
      },
    ],
    examples: [
      {
        input: '[22, 3, 15], 18228',
        result: '[1860, 13640, 2728]'
      },
      {
        input: '[8, 14, 11], 23541',
        result: '[10241, 5852, 7448]'
      },
      {
        input: '[8, 20, 17], 25281',
        result: '[13515, 5406, 6360]'
      },
    ]
  }),
  methods: {
    execute() {
      if(this.$refs.form.validate()) {
        this.loading = true
        this.axios.post('bonus_list', {days_absence: this.value.split(' '), bonus: this.bonus})
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
