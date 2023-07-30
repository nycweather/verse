export default function LoginPage() {
  return (
    <section className="bg-gray-900 text-white min-h-screen flex items-center justify-center">
      <div className="w-full max-w-md bg-gray-800 rounded-lg shadow-md">
        <div className="p-6 space-y-4">
          <h1 className="text-xl font-bold leading-tight">
            Sign in to your account
          </h1>
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
            <div className="flex items-center justify-between">
              <div className="flex items-start">
                <input
                  id="remember"
                  aria-describedby="remember"
                  type="checkbox"
                  className="checkbox-dark"
                  required
                />
                <label
                  htmlFor="remember"
                  className="ml-2 text-sm text-gray-300"
                >
                  Remember me
                </label>
              </div>
              <a
                href="#"
                className="text-sm font-medium text-blue-500 hover:underline"
              >
                Forgot password?
              </a>
            </div>
            <button type="submit" className="btn-primary-dark">
              Sign in
            </button>
            <p className="text-sm text-gray-300">
              Don’t have an account yet?{" "}
              <a href="/signup" className="font-medium text-blue-500 hover:underline">
                Sign up
              </a>
            </p>
          </form>
        </div>
      </div>
    </section>
  );
}
