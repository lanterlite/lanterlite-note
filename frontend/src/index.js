import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import ThemeDefault from './theme-default'
import injectTapEventPlugin from 'react-tap-event-plugin'
// Needed for onTouchTap http://stackoverflow.com/a/34015469/988941
import Route from './routes.js'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import { Provider } from 'react-redux'
import { createStore, combineReducers } from 'redux'
import { reducer as reduxFormReducer } from 'redux-form'

injectTapEventPlugin();

const reducer = combineReducers({
  form: reduxFormReducer // mounted under "form"
})

const store = (window.devToolsExtension
  ? window.devToolsExtension()(createStore)
  : createStore)(reducer)
window.store = store

ReactDOM.render(
    <Provider  store={store}>
        <MuiThemeProvider muiTheme={ThemeDefault}>
            <Route />
        </MuiThemeProvider>
    </Provider>,
  document.getElementById('root')
);
