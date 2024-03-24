<p>风险结算产品查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEPRODUCTSTATUS/">OnRspQryRiskSettleProductStatus</a></p>
<p>详见  <a href="../../../6.6.1P1BBGXSM/">6.6.1P1版本更新说明</a></p>
<span class="anchor" id="dba87143-5ffd-4d00-8c31-ef8e69bcd17e"></span>
## 1.函数原型
<p>virtual int ReqQryRiskSettleProductStatus(CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID) = 0;</p>
<span class="anchor" id="c0599588-2253-4ce3-93ae-baea4068e3d5"></span>
## 2.参数
<p>pQryRiskSettleProductStatus：风险结算产品查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4a17f178-fc6a-4d43-936e-d27e1feff4f3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="87cc9eac-80c4-4b38-bead-05656e189435"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="837c9302-e9f2-4845-b506-f976e9126c5d"></span>
## 5.FAQ
<p>无</p>
