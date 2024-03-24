<p>请求查询做市商合约手续费率</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYMMINSTRUMENTCOMMISSIONRATE/">OnRspQryMMInstrumentCommissionRate</a></p>
<span class="anchor" id="c27ca102-8c66-44ce-a2da-254e0e0fa0b2"></span>
## 1.函数原型
<p>virtual int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) = 0;</p>
<span class="anchor" id="eab0482e-9391-47d2-9b32-4c219634f615"></span>
## 2.参数
<p>pQryMMInstrumentCommissionRate：查询做市商合约手续费率</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="13dfb716-9ecf-40ff-beac-ecbf5e57a7f8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2e86cd28-1369-4dd2-b6d2-dc78be54a93c"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="3e6d75d2-0210-4823-9002-d333cd634ecb"></span>
## 5.FAQ
<p>无</p>
