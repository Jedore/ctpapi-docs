<p>请求查询投资者</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTOR/">OnRspQryInvestor</a></p>
<span class="anchor" id="bfce4f90-0858-43e8-b1e1-c23aaa61996d"></span>
## 1.函数原型
<p>virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;</p>
<span class="anchor" id="079d9ccf-84c9-4d76-8661-dbd56c71d712"></span>
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
<span class="anchor" id="e9326bde-32ac-4279-9fa1-05593ec568c1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d4923962-f181-4b9e-8b1e-2ec9c05431ed"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryInvestor(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="5f4912f8-2d3d-4e46-8755-a2f6eacabc78"></span>
## 5.FAQ
<p>无</p>
