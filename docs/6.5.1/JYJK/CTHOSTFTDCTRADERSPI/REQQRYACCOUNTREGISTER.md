<p>请求查询银期签约关系</p>
<p>响应: OnRspQryAccountregister</p>
<span class="anchor" id="78586825-be95-409f-8b3c-c03c74916481"></span>
## 1.函数原型
<p>virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;</p>
<span class="anchor" id="88133cbe-9362-4123-8d62-180d472e304f"></span>
## 2.参数
<p>pQryAccountregister：请求查询银期签约关系</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankBrchIDType</td>
<td style="TEXT-ALIGN: left;">BankBranchID</td>
<td style="TEXT-ALIGN: left;">银行分支机构代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>字段值填写正确时，均无查询结果</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="97777d90-dd24-4e4c-a0a2-f6c3a2f561c3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="476cb6e1-3d1e-4b32-9b02-4298357cee08"></span>
## 4.调用示例
<pre><code>CThostFtdcQryAccountregisterField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.BankID, "1");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryAccountregister(&amp;a, 1);
</code></pre>
<span class="anchor" id="ebbddf06-89bb-4c46-b18d-6e8721ed2a4a"></span>
## 5.FAQ
<p>无</p>
