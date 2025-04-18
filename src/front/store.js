export const initialStore=()=>{
  return{
    message: null,
    todos: [
      {
        id: 1,
        title: "Make the bed",
        background: null,
      },
      {
        id: 2,
        title: "Do my homework",
        background: null,
      }
    ],

    clients: [],
    isLoading: {
      clients:false
    },
    error:{
      clients:null
    }
  }
}

export default function storeReducer(store, action = {}) {
    switch(action.type){
    case 'set_hello':
      return {
        ...store,
        message: action.payload
      };
      
    case 'add_task':

      const { id,  color } = action.payload

      return {
        ...store,
        todos: store.todos.map((todo) => (todo.id === id ? { ...todo, background: color } : todo))
      };
    default:
      throw Error('Unknown action.');
      

    case"load_clients":
      return{
        ...store, 
        isLoading:{...store.isLoading,clients:true},
        error:{...store.error,clients:null}
      }
    

    case"set_clients":
      return{
        ...store, 
        clients:action.payload,
        isLoading:{...store.isLoading,clients:false},
        
      }
      case"client_error":
        return{
          ...store,
          error:{...store.error,clients:action.payload},
          isLoading:{...store.isLoading,clients:false},
        }

    }
  
}
