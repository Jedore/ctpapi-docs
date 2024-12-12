<p>风险结算产品查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEPRODUCTSTATUS/">OnRspQryRiskSettleProductStatus</a></p>
<p>详见  <a href="../../../6.6.1P1BBGXSM/">6.6.1P1版本更新说明</a></p>
<span class="anchor" id="a85d26ea-2e49-427a-95d1-aed8678b3a41"></span>
## 1.函数原型
<p>virtual int ReqQryRiskSettleProductStatus(CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID) = 0;</p>
<span class="anchor" id="721953db-7149-4c2c-b37a-de6c0fed6c5e"></span>
## 2.参数
<p>pQryRiskSettleProductStatus：风险结算产品查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e4050b21-ef47-4f58-bba9-6be2d558cbbd"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c8c2e188-54f8-499e-910d-f28d29bea622"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b396e9b3-723d-4af8-8b93-4911885e8ff6"></span>
## 5.FAQ
<p>无</p>
