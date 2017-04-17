import React from "react";
import ReactDOM from "react-dom";


export default class {{{name|capitalize}}}Component extends React.Component {
  static get defaultProps() {
    return {};
  }

  constructor(props) {
    super(props);
    this._validateProps();
    this._setupInitialState();
  }

  /* initialization functions */

  _validateProps() {
  }

  _setupInitialState() {
    this.state = {};
  }


  /* Render functions */

  render() {
    return <div></div>;
  }
}
