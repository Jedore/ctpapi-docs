<p>请求组合优惠比例，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBPROMOTIONPARAM/">OnRspQryCombPromotionParam</a></p>
<p>详见  <a href="../../../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p>
<span class="anchor" id="b1d3ddf3-7d8d-4606-867d-0a6794bb10db"></span>
## 1.函数原型
<p>virtual int ReqQryCombPromotionParam(CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID) = 0;</p>
<span class="anchor" id="9aa50991-356c-4e2a-bf2b-0ca31f3d0a5d"></span>
## 2.参数
<p>pQryCombPromotionParam：查询组合优惠比例</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="7978ee4d-9f65-4446-8aca-9d0539522323"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="684ff3b4-9284-49f8-86c7-6e811cfaba03"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2b1920fb-50ba-4a15-8855-4e95b240cede"></span>
## 5.FAQ
<p>无</p>
