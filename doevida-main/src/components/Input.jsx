
const Input = (props) => {
  return (
    <input placeholder={props.placeholder} type={props.type} className='rounded-2xl bg-gray-100 p-2 m-1.5 w-full mb-4 shadow-sm' id={props.id} onChange={props.onChange}/>
  )
}

export default Input