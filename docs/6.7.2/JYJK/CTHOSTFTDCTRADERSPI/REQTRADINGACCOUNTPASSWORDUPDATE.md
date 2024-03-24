<p>资金账户口令更新请求，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPTRADINGACCOUNTPASSWORDUPDATE/">OnRspTradingAccountPasswordUpdate</a>。</p>
<span class="anchor" id="d3b40df5-d1a3-47d8-b059-25614f85287d"></span>
## 1.函数原型
<p>virtual int ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) = 0;</p>
<span class="anchor" id="2deddb80-5130-4f89-af8c-1d528db815d7"></span>
## 2.参数
<p>pTradingAccountPasswordUpdate：资金账户口令变更域</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">OldPassword</td>
<td style="TEXT-ALIGN: left;">原来的口令</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">NewPassword</td>
<td style="TEXT-ALIGN: left;">新的口令</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b3fcf80b-1839-4abf-a413-457a941a4dad"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1aa0943a-8635-4412-af3b-e7d1ffac4ed0"></span>
## 4.调用示例
<pre><code>CThostFtdcTradingAccountPasswordUpdateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.OldPassword, "123456");
strcpy_s(a.NewPassword, "666666");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqTradingAccountPasswordUpdate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="d0425509-2042-4a6e-bb49-8a709aeecad4"></span>
## 5.FAQ
<p>无</p>
