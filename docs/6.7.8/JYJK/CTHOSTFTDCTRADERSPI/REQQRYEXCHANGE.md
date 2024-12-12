<p>请求查询交易所</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGE/">OnRspQryExchange</a></p>
<span class="anchor" id="78298569-5c07-482e-9207-094b6c1c94f2"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="fe34069b-6f84-4daf-81df-33ceff2c48b8"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="dcbd3867-5554-4776-b14e-eaff27842012"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="14628f04-2566-438e-bb79-f7c0b1c3f95d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c9413e12-fbf8-431c-86f9-a7c212e2dde9"></span>
## 5.FAQ
<p>无</p>
