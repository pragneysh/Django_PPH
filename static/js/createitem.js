const [title, setTitle] = useState("");
const [calories, setCalories] = useState("");
const [price, setPrice] = useState("");
const [category, setCategory] = useState(null);
const [imageAsset, setImageAsset] = useState(null);
const [fields, setFields] = useState(false);
const [alertStatus, setAlertStatus] = useState("danger");
const [msg, setMsg] = useState(null);
const [isLoading, setIsLoading] = useState(false);
const [{ foodItems }, dispatch] = useStateValue();

{
    fields && (
        <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className={`w-full p-2 rounded-lg text-center text-lg font-semibold ${alertStatus === "danger"
                    ? "bg-red-400 text-red-800"
                    : "bg-emerald-400 text-emerald-800"
                }`}
        >
            {msg}
        </motion.p>
    )
}