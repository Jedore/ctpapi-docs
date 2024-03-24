<p>请求SPBM期货合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a></p>
<span class="anchor" id="04d77306-1b40-40fe-8149-8b00f32686da"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMFutureParameter(CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID) = 0;</p>
<span class="anchor" id="2e986e27-b82a-4fd3-8c65-b60230024d89"></span>
## 2.参数
<p>pQrySPBMFutureParameter：SPBM期货合约保证金参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="41f77747-cbc7-445b-aac7-0010fb2350f9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b84c92c7-6681-4e66-a0ae-af302143e74e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f00f123f-ac76-4b22-a2b0-8ced91e5f889"></span>
## 5.FAQ
<p>无</p>
