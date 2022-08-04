- slice
  - import { createSlice } from '@reduxjs/toolkit'
  - store 안의 작은 store
  - 여러개 만들면 된다

```jsx
const counterSlice(이름) = createSlice ({
    name : 이름
    initialState : {key:value} 초기값 필요
    reducers : {
        up(액션타입) : { state, action } => {
    state.valuue = state.value + action.step(변경할것);
}
}
});
```

- configureStore
  - import { configureStore } from '@reduxjs/toolkit'
  - 작은 slice 모아서 store로 만들 때

```jsx
configureStore({
    객체 전달 ~ 
    reducer : {
        각각의 slice의 reducer들이 들어가면 된다.
        // counter에 대한 reducer다~!
        counter : counterSlice.reducer 
    }
});
```

=> 이렇게 만들어진게 store!

- provider로 store 전달하면 된다!

```js
<Provider store={store}> 

</Provider>
```

- useSelector
  - store에서 사용하는 여러가지 state 사용하려면 사용!

```jsx
function Counter(){

    const dispatch = useDispatch();
    const count = useSelector(state => {
        // console.log(state); // 열어보는 용도 ,, 
        // store에 들어간 reducer 이름 뜬다 

        // counterSlice안의 value값
        return state.counter.value;

});
}
    
dispatch({type: 'counterSlice/up' '슬라이스이름/counter'})
```