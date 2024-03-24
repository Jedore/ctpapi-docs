<p>风险结算产品查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEPRODUCTSTATUS/">OnRspQryRiskSettleProductStatus</a></p>
<p>详见  <a href="../../../6.6.1P1BBGXSM/">6.6.1P1版本更新说明</a></p>
<span class="anchor" id="cba93da8-b3b6-4d28-9f01-9dbc98e22688"></span>
## 1.函数原型
<p>virtual int ReqQryRiskSettleProductStatus(CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID) = 0;</p>
<span class="anchor" id="0bc338fa-88eb-4e87-9e37-3adc94ed6953"></span>
## 2.参数
<p>pQryRiskSettleProductStatus：风险结算产品查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="94b30eb1-0cb0-449a-aa22-5bb5ab5bf48e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c1ce131e-5ee2-4402-9d07-17290e6fda95"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="825424f2-3ef1-40a6-85a8-3aa33185fc0f"></span>
## 5.FAQ
<p>无</p>
