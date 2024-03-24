<p>请求组合优惠比例，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBPROMOTIONPARAM/">OnRspQryCombPromotionParam</a></p>
<p>详见  <a href="../../../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p>
<span class="anchor" id="27c555bb-991c-4b39-bd67-8fb0b9d12f07"></span>
## 1.函数原型
<p>virtual int ReqQryCombPromotionParam(CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID) = 0;</p>
<span class="anchor" id="68373470-be62-4489-8a7c-daf41d5ce32d"></span>
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
<span class="anchor" id="46258278-fa04-4b80-ac99-77974ee8ac94"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="05794d44-f1c8-42cc-a248-01d9cc026232"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8ab1a97a-c0f9-4e6d-afbc-3fefc4dfb474"></span>
## 5.FAQ
<p>无</p>
