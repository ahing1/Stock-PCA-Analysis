# Use the official Node.js image as the base
FROM node:18 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code and build the React app
COPY . .
RUN npm run build

# Use Node.js to serve the app
FROM node:18 AS server

# Set the working directory
WORKDIR /app

# Install serve to serve the React build
RUN npm install -g serve

# Copy the built app from the builder
COPY --from=builder /app/dist ./dist

# Expose the port required by Google Cloud Run
ENV PORT 8080
EXPOSE 8080

# Command to serve the app on the Cloud Run-provided PORT
CMD ["serve", "-s", "dist", "-l", "8080"]

