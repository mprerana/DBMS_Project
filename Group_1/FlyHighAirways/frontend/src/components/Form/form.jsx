// import React, { Component } from "react";

// import { Form, Input, Icon, Button } from "antd";

// let id = 0;

// class DynamicFieldSet extends React.Component {
//   remove = k => {
//     const { form } = this.props;
//     // can use data-binding to get
//     const keys = form.getFieldValue("keys");
//     // We need at least one passenger
//     if (keys.length === 1) {
//       return;
//     }

//     // can use data-binding to set
//     form.setFieldsValue({
//       keys: keys.filter(key => key !== k)
//     });
//   };

//   add = () => {
//     const { form } = this.props;
//     // can use data-binding to get
//     const keys = form.getFieldValue("keys");
//     const nextKeys = keys.concat(id++);
//     // can use data-binding to set
//     // important! notify form to detect changes
//     form.setFieldsValue({
//       keys: nextKeys
//     });
//   };

//   handleSubmit = e => {
//     e.preventDefault();
//     this.props.form.validateFields((err, values) => {
//       if (!err) {
//         const { keys, names } = values;
//         console.log("Received values of form: ", values);
//         console.log("Merged values:", keys.map(key => names[key]));
//       }
//     });
//   };

//   render() {
//     const { getFieldDecorator, getFieldValue } = this.props.form;
//     const formItemLayout = {
//       labelCol: {
//         xs: { span: 24 },
//         sm: { span: 4 }
//       },
//       wrapperCol: {
//         xs: { span: 24 },
//         sm: { span: 20 }
//       }
//     };
//     const formItemLayoutWithOutLabel = {
//       wrapperCol: {
//         xs: { span: 24, offset: 0 },
//         sm: { span: 20, offset: 4 }
//       }
//     };
//     getFieldDecorator("keys", { initialValue: [] });
//     const keys = getFieldValue("keys");
//     const formItems = keys.map((k, index) => (
//       <Form.Item
//         {...(index === 0 ? formItemLayout : formItemLayoutWithOutLabel)}
//         label={index === 0 ? "Passengers" : ""}
//         required={false}
//         key={k}
//       >
//         {getFieldDecorator(`names[${k}]`, {
//           validateTrigger: ["onChange", "onBlur"],
//           rules: [
//             {
//               required: true,
//               whitespace: true,
//               message: "Please input passenger's name or delete this field."
//             }
//           ]
//         })(
//           <Input
//             placeholder="passenger name"
//             style={{ width: "60%", marginRight: 8 }}
//           />
//         )}
//         {keys.length > 1 ? (
//           <Icon
//             className="dynamic-delete-button"
//             type="minus-circle-o"
//             disabled={keys.length === 1}
//             onClick={() => this.remove(k)}
//           />
//         ) : null}
//       </Form.Item>
//     ));
//     return (
//       <Form onSubmit={this.handleSubmit}>
//         {formItems}
//         <Form.Item {...formItemLayoutWithOutLabel}>
//           <Button type="dashed" onClick={this.add} style={{ width: "60%" }}>
//             <Icon type="plus" /> Add field
//           </Button>
//         </Form.Item>
//         <Form.Item {...formItemLayoutWithOutLabel}>
//           <Button type="primary" htmlType="submit">
//             Submit
//           </Button>
//         </Form.Item>
//       </Form>
//     );
//   }
// }
// export default DynamicFieldSet;

// // const WrappedDynamicFieldSet = Form.create({ name: "dynamic_form_item" })(
// //   DynamicFieldSet
// // );
// // ReactDOM.render(<WrappedDynamicFieldSet />, mountNode);
// // // class  extends Component {
// //     state = {  }
// //     render() {
// //         return (  );
// //     }
// // }

import React from "react";
import CatInputs from "./CatInputs";
class Form extends React.Component {
  state = {
    cats: [{ name: "", age: "" }],
    owner: "",
    description: ""
  };
  handleChange = e => {
    if (["name", "age"].includes(e.target.className)) {
      let cats = [...this.state.cats];
      cats[e.target.dataset.id][
        e.target.className
      ] = e.target.value.toUpperCase();
      this.setState({ cats }, () => console.log(this.state.cats));
    } else {
      this.setState({ [e.target.name]: e.target.value.toUpperCase() });
    }
  };
  addCat = e => {
    this.setState(prevState => ({
      cats: [...prevState.cats, { name: "", age: "" }]
    }));
  };
  handleSubmit = e => {
    e.preventDefault();
  };
  render() {
    let { owner, description, cats } = this.state;
    return (
      <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
        <label htmlFor="name">Owner</label>
        <input type="text" name="owner" id="owner" value={owner} />
        <label htmlFor="description">Description</label>
        <input
          type="text"
          name="description"
          id="description"
          value={description}
        />
        <button onClick={this.addCat}>Add new cat</button>
        <CatInputs cats={cats} />
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
export default Form;
