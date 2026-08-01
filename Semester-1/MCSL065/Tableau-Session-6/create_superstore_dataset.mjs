import fs from 'node:fs/promises';

const regions = [
  ['West', 1.34], ['East', 1.22], ['Central', 1.13], ['South', 1.05],
  ['North', 0.98], ['Northeast', 0.93], ['Northwest', 0.88],
  ['Southeast', 0.84], ['Southwest', 0.79],
];
const products = [
  ['Furniture', 'Chairs', 'Ergonomic Office Chair', 340],
  ['Furniture', 'Tables', 'Adjustable Work Table', 420],
  ['Furniture', 'Bookcases', 'Wooden Storage Bookcase', 275],
  ['Office Supplies', 'Binders', 'Premium Ring Binder', 28],
  ['Office Supplies', 'Paper', 'Multipurpose Copy Paper', 18],
  ['Office Supplies', 'Storage', 'Stackable Storage Box', 46],
  ['Technology', 'Phones', 'Business Smartphone', 560],
  ['Technology', 'Accessories', 'Wireless Keyboard', 78],
  ['Technology', 'Machines', 'Desktop Printer', 390],
];
const segments = ['Consumer', 'Corporate', 'Home Office'];
let seed = 20260719;
const random = () => {
  seed = (seed * 1664525 + 1013904223) >>> 0;
  return seed / 4294967296;
};
const csvCell = (value) => `"${String(value).replaceAll('"', '""')}"`;
const headers = [
  'Row ID', 'Order ID', 'Order Date', 'Region', 'Customer ID', 'Segment',
  'Category', 'Sub-Category', 'Product Name', 'Sales', 'Advertising Expenditure',
  'Customer Visits', 'Product Price', 'Quantity', 'Discount', 'Profit',
];
const rows = [];
let rowId = 1;
for (let month = 0; month < 12; month += 1) {
  for (let r = 0; r < regions.length; r += 1) {
    const [region, regionFactor] = regions[r];
    const [category, subCategory, productName, basePrice] = products[(month + r * 2) % products.length];
    const quantity = 1 + Math.floor(random() * (category === 'Office Supplies' ? 9 : 4));
    const discount = [0, 0, 0.05, 0.1, 0.15, 0.2][Math.floor(random() * 6)];
    const seasonalFactor = 0.86 + month * 0.025 + random() * 0.18;
    const price = Math.round(basePrice * (0.92 + random() * 0.16) * 100) / 100;
    const sales = Math.round(price * quantity * (1 - discount) * regionFactor * seasonalFactor * 100) / 100;
    const advertising = Math.round((sales * (0.045 + random() * 0.045) + 30) * 100) / 100;
    const visits = Math.max(12, Math.round(18 + quantity * 7 + random() * 55 + r * 2));
    const margin = category === 'Technology' ? 0.28 : category === 'Furniture' ? 0.22 : 0.18;
    const profit = Math.round((sales * (margin - discount * 0.65) - advertising * 0.32) * 100) / 100;
    const day = 2 + ((r * 3 + month * 2) % 26);
    const orderDate = `2025-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    rows.push([
      rowId, `ORD-2025-${String(rowId).padStart(4, '0')}`, orderDate, region,
      `CUST-${String(1000 + ((rowId * 17) % 300)).padStart(4, '0')}`,
      segments[(rowId + month) % segments.length], category, subCategory, productName,
      sales.toFixed(2), advertising.toFixed(2), visits, price.toFixed(2), quantity,
      discount.toFixed(2), profit.toFixed(2),
    ]);
    rowId += 1;
  }
}
const content = [headers, ...rows].map((row) => row.map(csvCell).join(',')).join('\n') + '\n';
await fs.writeFile('Superstore.csv', content, 'utf8');
console.log(`Created Superstore.csv with ${rows.length} rows, 12 months, and ${regions.length} regions.`);
