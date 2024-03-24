<p>请求查询投资者</p>
<p>响应：OnRspQryInvestor</p>
<span class="anchor" id="564c99e7-f057-4067-af3a-d39cb69d9b4f"></span>
## 1.函数原型
<p>virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;</p>
<span class="anchor" id="726afe74-d6fa-41c2-9ad5-093fed2a6227"></span>
## 2.参数
<p>pQryInvestor：查询投资者</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="78c0f332-3b17-411d-ade9-ab97de3ca44d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="58837a50-7a08-4470-b97c-462231c3a7ac"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryInvestor(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="dbb4d60d-8614-44c3-a3b0-eb69888c6618"></span>
## 5.FAQ
<p>无</p>
