<p>请求查询交易通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADINGNOTICE/">OnRspQryTradingNotice</a></p>
<span class="anchor" id="f099a405-547c-4b64-b9f9-68dece5315fe"></span>
## 1.函数原型
<p>virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;</p>
<span class="anchor" id="47a628e7-4cb1-4104-96ba-e5137145a0db"></span>
## 2.参数
<p>pQryTradingNotice：查询交易事件通知</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="098179d1-81b1-48b4-91ba-753472e528e7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6b888fcc-7175-4667-93e8-bf963a89188d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="815e81f7-ba8c-4b5f-8aa7-c7c18eea9e64"></span>
## 5.FAQ
<p>无</p>
