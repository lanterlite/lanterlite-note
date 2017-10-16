import getMuiTheme from 'material-ui/styles/getMuiTheme'
import * as Color from 'material-ui/styles/colors'

const themeDefault = getMuiTheme({
    fontFamily: 'Lato, sans-serif',
    palette: {
        backgroundColor: Color.grey50
    },
    appBar: {
        height: 57,
        color: Color.blue900
    },
    drawer: {
        width: 250,
    },
    raisedButton: {
        primaryColor: Color.blue500,
        secondaryColor: Color.cyan400
    }
})

export default themeDefault;
