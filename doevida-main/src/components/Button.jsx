
const Button = (props) => {
  return (
    <button className="bg-[#9d1717] p-1.5 m-2 rounded-2xl w-full text-gray-50 cursor-pointer hover:bg-[#9d1717b2] mb-2" id={props.id} onClick={props.onClick} type={props.type}>
        {props.text}
    </button>
  )
}

export default Button