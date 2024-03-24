<p>请求组合优惠比例，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBPROMOTIONPARAM/">OnRspQryCombPromotionParam</a></p>
<p>详见  <a href="../../../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p>
<span class="anchor" id="77e00d52-0db3-45d3-93c8-ec3ea0189c54"></span>
## 1.函数原型
<p>virtual int ReqQryCombPromotionParam(CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID) = 0;</p>
<span class="anchor" id="92195493-bfec-4606-a325-2dd6aa8393e1"></span>
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
<span class="anchor" id="741b8194-be80-47c7-8a39-19436d840542"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="53c6184c-8980-4972-9f0f-4bf2929fa677"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ba4ff5fc-fab5-4f23-9498-44cadae10da7"></span>
## 5.FAQ
<p>无</p>
