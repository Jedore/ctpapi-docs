<p>风险结算产品查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEPRODUCTSTATUS/">OnRspQryRiskSettleProductStatus</a></p>
<p>详见  <a href="../../../6.6.1P1BBGXSM/">6.6.1P1版本更新说明</a></p>
<span class="anchor" id="37e3f636-4752-4472-85c9-aba02fee7e66"></span>
## 1.函数原型
<p>virtual int ReqQryRiskSettleProductStatus(CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID) = 0;</p>
<span class="anchor" id="dcbd22d8-2ff7-420c-b32f-a8006537f5b1"></span>
## 2.参数
<p>pQryRiskSettleProductStatus：风险结算产品查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="dc29cf6e-3041-4b69-852e-d069f06f5b24"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ffa6b5c6-5244-413c-9cd0-8126fdb644f7"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="69b04646-da95-4bda-a866-01565aff832e"></span>
## 5.FAQ
<p>无</p>
