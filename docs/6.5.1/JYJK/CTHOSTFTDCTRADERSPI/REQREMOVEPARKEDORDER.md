<p>请求删除预埋单，对应响应OnRspRemoveParkedOrder。该函数用于删除已经报入但未触发的某笔预埋报单，注意跟ReqRemoveParkedOrderAction的区别。</p>
<span class="anchor" id="4849f2f1-34f3-4b95-b6e2-947fd31bfc9a"></span>
## 1.函数原型
<p>virtual int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) = 0;</p>
<span class="anchor" id="16aa4b6b-25f9-48d1-a53e-4d2f7b614ecb"></span>
## 2.参数
<p>pRemoveParkedOrder：删除预埋单</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParkedOrderIDType</td>
<td style="TEXT-ALIGN: left;">ParkedOrderID</td>
<td style="TEXT-ALIGN: left;">预埋报单编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>ParkedOrderID：对应的预埋报单编号，指定要删除的预埋报单。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="cff8b4ae-2d18-4bce-8f3a-c901c9709057"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b631ab83-7d0e-431b-883f-caec3529715e"></span>
## 4.示例调用
<pre><code>CThostFtdcRemoveParkedOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ParkedOrderID, "           5");
m_pUserApi-&gt;ReqRemoveParkedOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="e5036987-804b-42b0-a940-16a04d3cfa25"></span>
## 5.FAQ
<p>无</p>
