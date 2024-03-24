<p>请求组合优惠比例，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBPROMOTIONPARAM/">OnRspQryCombPromotionParam</a></p>
<p>详见  <a href="../../../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p>
<span class="anchor" id="11762dd5-97ad-4efc-84ad-acdb7143ca25"></span>
## 1.函数原型
<p>virtual int ReqQryCombPromotionParam(CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID) = 0;</p>
<span class="anchor" id="0373740c-1f73-4539-b7c0-b7ca685c3b64"></span>
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
<span class="anchor" id="97de2085-d9ca-4daf-9330-c5560982a45b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d4250aef-2c56-4fe4-9d2a-5f0807dc57d3"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8d49092b-317b-4f1a-ba81-4e1fdba0b939"></span>
## 5.FAQ
<p>无</p>
