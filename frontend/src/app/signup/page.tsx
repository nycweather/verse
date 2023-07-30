import link from "next/link";

export default function SignupPage() {
  return (
    <section className="bg-gray-900 text-white min-h-screen flex items-center justify-center">
      <div className="w-full max-w-md bg-gray-800 rounded-lg shadow-md">
        <div className="p-6 space-y-4">
          <h1 className="text-xl font-bold leading-tight">Create an account</h1>
          <form className="space-y-4" action="#">
            <div>
              <label htmlFor="email" className="block mb-2 text-sm font-medium">
                Your email
              </label>
              <input
                type="email"
                name="email"
                id="email"
                className="input-dark"
                placeholder="name@company.com"
                required
              />
            </div>
            <div>
              <label
                htmlFor="password"
                className="block mb-2 text-sm font-medium"
              >
                Password
              </label>
              <input
                type="password"
                name="password"
                id="password"
                className="input-dark"
                placeholder="••••••••"
                required
              />
            </div>
            <div>
              <label
                htmlFor="confirm-password"
                className="block mb-2 text-sm font-medium"
              >
                Confirm password
              </label>
              <input
                type="password"
                name="confirm-password"
                id="confirm-password"
                className="input-dark"
                placeholder="••••••••"
                required
              />
            </div>
            <div className="flex items-start">
              <div className="flex items-center h-5">
                <input
                  id="terms"
                  aria-describedby="terms"
                  type="checkbox"
                  className="checkbox-dark"
                  required
                />
              </div>
              <div className="ml-3 text-sm">
                <label htmlFor="terms" className="font-light text-gray-300">
                  I accept the{" "}
                  <a
                    className="font-medium text-blue-500 hover:underline"
                    href="#"
                  >
                    Terms and Conditions
                  </a>
                </label>
              </div>
            </div>
            <button type="submit" className="btn-primary-dark">
              Create an account
            </button>
            <p className="text-sm text-gray-300">
              Already have an account?{" "}
              <a href="/login" className="font-medium text-blue-500 hover:underline">
                Login here
              </a>
            </p>
          </form>
        </div>
      </div>
    </section>
  );
}
