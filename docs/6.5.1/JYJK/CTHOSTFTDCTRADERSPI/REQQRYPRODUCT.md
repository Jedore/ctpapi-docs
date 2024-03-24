<p>请求查询产品</p>
<p>响应: OnRspQryProduct</p>
<span class="anchor" id="99c3278f-d57c-4faf-8ba3-c48dc9837f42"></span>
## 1.函数原型
<p>virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;</p>
<span class="anchor" id="bc356665-8771-4d32-99bf-73800f0de02c"></span>
## 2.参数
<p>pQryProduct：查询产品</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">产品类型</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductClassType</td>
<td style="TEXT-ALIGN: left;">ProductClass</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="40e6c73e-8547-44ed-bb25-59e7c2369ebb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a16b808b-aba7-4662-8d42-9510faa19cfc"></span>
## 4.调用示例
<pre><code>CThostFtdcQryProductField a = { 0 };
strcpy_s(a.ProductID, "sc");
a.ProductClass = THOST_FTDC_PC_Futures;
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryProduct(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="9d92d3fc-1c8c-4e5b-b4ab-9278f025cd42"></span>
## 5.FAQ
<p>无</p>
